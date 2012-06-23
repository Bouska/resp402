# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    holds = models.ManyToManyField("self", symmetrical=False)

class CategoryItem(models.Model):
    category = models.ForeignKey(Category)
    object_id = models.PositiveIntegerField()
    object_content = models.ForeignKey(ContentType)
    thing = GenericForeignKey('object_content', 'object_id')
    priority = models.PositiveIntegerField()
