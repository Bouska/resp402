# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models

class Thread(models.Model):
    subject = models.TextField();
    user = models.ForeignKey(User)
    refer_oid = models.PositiveIntegerField()
    refer_content = models.ForeignKey(ContentType)
    referer = GenericForeignKey('refer_content', 'refer_oid')

class Message(models.Model):
    user = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    reference = models.ForeignKey("self", null=True)
