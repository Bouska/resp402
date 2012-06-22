# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.shortcuts import get_object_or_404
from www.json import json_object, json_send
from django.contrib.auth.models import User

@json_send
def my_profile(request):
    return json_object(request, request.user, ['id', 'username', 
                ('get_profile.real_name', 'realname'),
                ('get_profile.registration', 'registration'),])

@json_send
def some_profile(request, object_id):
    user = get_object_or_404(User, object_id)
    return json_object(request, user, ['id', 'username',
                ('get_profile.real_name', 'realname')])
