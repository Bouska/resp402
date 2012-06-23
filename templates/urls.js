/* {% comment %}
Copyright 2011, hast. All rights reserved.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.
{% endcomment %} */

/* {% comment %}
from django.core.urlresolvers import get_resolver

sorted([
	(key, value[0][0][0])
	for key, value in get_resolver(None).reverse_dict.items()
	if isinstance(key, basestring)
])
{% endcomment %} */

urls = {
    'application': 'zoidberg',
    'auth_entry': function(a) { return 'auth/' + a; },
    'index': '',
    'logout': 'logout',
    'syslogin': 'syslogin',
    'profile_get': function(a) { return 'profile/get/' + a },
    'profile_me': 'profile/me',
    'category_get': function(a) { return 'category/get/' + a},
};
