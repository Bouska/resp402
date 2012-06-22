# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls.defaults import patterns, url
from www.authentification import stop_anon
from profile.views import my_profile, some_profile

urlpatterns = patterns('',
    url(r'^me$', 
        stop_anon(my_profile), 
        name='profile_me'),

    url(r'^get/(?P<object_id>[^/]+)$',
        stop_anon(some_profile),
        name='profile_get'),
)
