# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime

### Magic begins here
# The goal is to make a single class Notif agregating avery notif type below.
# We use metaclass and dynamic models creation to avoid the use of polymorphic
# models (inheritance in orm sux, see vietnam of computer sciences)

action_fields, output_method, urls_method = dict(), dict(), dict()

def check_field(name, value):
    if name in action_fields:
        if isinstance(value, models.ForeignKey):
            if action_fields[name].rel.to != value.rel.to:
                raise Exception("Action model error, ForeignKey %s incoherent" % name)
        elif action_fields[name] != value:
            raise Exception("Action model error, value %s incoherent" % name)
        elif name == "type" or name == "date" or name == "url":
            raise Exception("Action model error, name %s forbidden" % name)
    else:
        return True

def create_notif():
    class Meta:
        app_label = 'notifications'

    def to_string(self):
        return self._output[self.type](self)

    def to_url(self):
        return self._urls[self.type](self)

    action_fields['Meta'] = Meta
    action_fields['type'] = models.CharField(max_length=100)
    action_fields['date'] = models.DateTimeField(default=datetime.now)
    action_fields['_output'] = output_method
    action_fields['_urls'] = urls_method
    action_fields['__module__'] = 'notifications'
    action_fields['__str__'] = to_string
    action_fields['__unicode__'] = to_string
    action_fields['url'] = to_url
    
    return type('Notif', (models.Model,), action_fields)

class MetaNotif(type):
    def __init__(cls, name, bases, fields):
        for attr, value in fields.iteritems():
            if attr.startswith('_'):
                continue
            if check_field(attr, value):
                action_fields[attr] = value
        
        output_method[cls.__name__] = fields['__str__']
        urls_method[cls.__name__] = fields['_url']

class BaseNotif(object):
    @classmethod
    def throw(cls, *args, **kwargs):
        notif = Notif(*args, **kwargs)
        notif.type = cls.__name__
        notif.save()
        return notif

### Magic ends here.
# You can declare your models as usual, anything based on BaseNotif
# will be integrated in the Notif model.

class UploadNotif(BaseNotif):
    __metaclass__ = MetaNotif
    context = models.ForeignKey('courses.Course', null=True)
    user = models.ForeignKey(User, null=True)
    document = models.ForeignKey('documents.Document', null=True)

    def __str__(self):
        return "%s uploaded a new document %s" % (self.user.username, 
                                                  self.document.name)
    
    def _url(self):
        return reverse('view_file', args=[self.document.id])

class ThreadNotif(BaseNotif):
    __metaclass__ = MetaNotif
    context = models.ForeignKey('courses.Course', null=True)
    user = models.ForeignKey(User, null=True)
    thread = models.ForeignKey('messages.Thread', null=True)

    def __str__(self):
        return "%s opened a new thread about %s" % (self.user.username,
                                                    self.thread.subject)
    
    def _url(self):
        return reverse('thread_view', args=[self.thread.id])

class ReplyNotif(BaseNotif):
    __metaclass__ = MetaNotif
    context = models.ForeignKey('courses.Course', null=True)
    user = models.ForeignKey(User, null=True)
    thread = models.ForeignKey('messages.Thread', null=True)

    def __str__(self):
        return "%s replied to the thread about %s" % (self.user.username,
                                                      self.thread.subject)

    def _url(self):
        return reverse('thread_view', args=[self.thread.id])

class Announcement(BaseNotif):
    __metaclass__ = MetaNotif
    user = models.ForeignKey(User, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return "%s %s : %s" % (self.user.first_name, self.user.last_name, 
                               self.content)

    def _url(self):
        return '#'

# don't touch that
Notif = create_notif()
