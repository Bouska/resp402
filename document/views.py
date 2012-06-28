# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.shortcuts import get_object_or_404
from www.json import json_send

@json_send
def upload_file(request):
    return '{"message": "ok"}'

@json_send
def upload_http(request):
    return '{"message": "ok"}'
