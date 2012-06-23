# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.db import models

class Course(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

class CourseURL(models.Model):
    course = models.ForeignKey(Course)
    url = models.TextField()
    name = models.TextField()
    click = models.PositiveIntegerField(default=0)
