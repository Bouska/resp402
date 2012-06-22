# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class WordEntry(models.Model):
    word = models.TextField();
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    thing = generic.GenericForeignKey('content_type', 'object_id')
    count = models.IntegerField()
    click = models.IntegerField(default=2)

    class Meta:
        unique_together = ('word', 'content_type', 'object_id')
