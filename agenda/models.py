# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    context_oid = models.PositiveIntegerField()
    context_content = models.ForeignKey(ContentType)
    context = GenericForeignKey('context_content', 'context_oid')
    added_by = models.ForeignKey(User)
