#!/usr/bin/env python

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from os import environ
environ.setdefault('DJANGO_SETTINGS_MODULE', 'www.settings')


from course.models import Course

Course.objects.create(slug='info-f-666', name='Hell Informatique', 
                      description='Hell Computer Science course')
Course.objects.create(slug='math-h-708', name='Over Math', 
                      description='New math course based on fuzzy axiomes')
