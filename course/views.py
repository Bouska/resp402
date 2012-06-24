# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.shortcuts import get_object_or_404
from www.json import json_send, json_list, json_object
from course.models import Course, CourseURL

@json_send
def get_course(r, slug):
    course = get_object_or_404(Course, slug=slug)
    res = [ json_object(r, course, ['id', 'name', 
                                          'description', 'slug'])[1:-1],
            '"urls": ' + json_list(r, CourseURL.objects.filter(course=course),
                                 ['url', 'name', 'click'])]
    return '{' + ', '.join(res) + '}'
