# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.contrib.auth.models import User
from django.db import models

META_ROLE = ['Leader', 'Accounting', 'Administrator', 'Party', 'Academique', 
             'Other'] # todo

class Group(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(null=True)

class GroupMember(models.Model):
    user = models.ForeignKey(User)
    title = models.TextField()
    meta = models.TextField()

class GroupURL(models.Model):
    group = models.ForeignKey(Group)
    url = models.TextField()
    name = models.TextField()
    click = models.PositiveIntegerField(default=0)

class Publication(models.Model):
    group = models.ForeignKey(Group)
    slug = models.CharField(unique=True, max_length=250)
    subject = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User)
