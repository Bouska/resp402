# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls.defaults import patterns, url
from www.authentification import stop_anon
from category.views import get_category

urlpatterns = patterns('',
    url(r'^get/(?P<object_id>[^/]+)$', stop_anon(get_category), 
        name='category_get'),
)
