# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls.defaults import patterns, url
from www.authentification import stop_anon
from www.json import json_send, json_list
from document.models import Document

urlpatterns = patterns('',
    url(r'^all$', stop_anon(json_send(json_list)), 
        {'queryset': Document.objects.all,
         'fields': ['id', 'name', 'description']},
        name='document_all'),
)
