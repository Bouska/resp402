# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls import patterns, url, include
from django.views.generic.simple import direct_to_template
from authentification import app_redirection, ulb_redirection, intranet_auth
from django.contrib.auth.views import login, logout
from settings import OBJECT_FILE


# decorator whom call function_in if user is authenticated, function_out if not
def user_logged(function_in, function_out):
    def toggle(request, *args, **kwargs):
        if request.user.is_authenticated():
            return function_in(request, *args, **kwargs)
        else:
            return function_out(request, *args, **kwargs)
    return toggle


urlpatterns = patterns('',
    # Plateforme URLS, here we include all the things outputing json
    url(r'^course/', include('course.urls'), name='course'),
    url(r'^document/', include('document.urls'), name='document'),


    # The product/client entry points
    url(r'^$',
        user_logged(app_redirection, direct_to_template),
        {'template': 'index.html'},
        name='index'),

    url(r'^zoidberg$',
        user_logged(direct_to_template, ulb_redirection),
        {'template': 'application.html',
         'extra_context': {'objects': OBJECT_FILE}},
        name='application'),

    url(r'^syslogin$',
        user_logged(app_redirection, login),
        {'template_name': 'syslogin.html'},
        name='syslogin'),

    url(r'^auth/(?P<next_url>.*)$',
        intranet_auth,
        name='auth_entry'),

    url(r'^logout$',
        logout, {'next_page': '/'}, 
        name="logout"),
)
