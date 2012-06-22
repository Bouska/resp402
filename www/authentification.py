# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import login
from django.utils.html import escape
from xml.dom.minidom import parseString
from profile.models import Inscription
from string import printable
from random import choice
from settings import ULB_AUTH, ULB_LOGIN
from urllib2 import urlopen
from base64 import b64encode

# redirect user to ulb intranet auth in respect of the url
def ulb_redirection(request, **kwargs):
    return render_to_response('redirection.html', {'url': ULB_LOGIN},
                              context_instance=RequestContext(request))

# redirect user to internal/his profile
def app_redirection(request, **kwargs):
    return HttpResponseRedirect(reverse('application'))


def get_text(nodelist):
    rc = [ node.data for node in nodelist if node.nodeType == node.TEXT_NODE ]
    return ''.join(rc)

def get_value(dom, name):
    nodes = dom.getElementsByTagName(name)
    real_node, found = None, 0
    if len(nodes) != 1:
        for n in nodes:
            if found:
                break
            for child in n.parentNode.childNodes:
                if child.nodeName == name:
                    real_node = child
                if (child.nodeName == 'status' and 
                    get_text(child.childNodes) == 'registered'):
                    found = 1
        if found == 0:
            raise Exception("xml document not conform for " + name)
    else:
        real_node = nodes[0]
    return escape(get_text(real_node.childNodes))

def parse_user(raw):
    dom = parseString(raw)
    return {
        'ip': get_value(dom, "ipAddress"),
        'username': get_value(dom, "username"),
        'first_name': get_value(dom, "prenom").capitalize(),
        'last_name': get_value(dom, "nom").capitalize(),
        'email': get_value(dom, "email"),
        'registration': get_value(dom, "matricule"),
        'anet': get_value(dom, "anet"),
        'anac': get_value(dom, "anac"),
        'facid': get_value(dom, "facid"),
    }

def create_user(values):
    try:
        user = User.objects.get(username=values['username'])
    except:
        rpwd = ''.join(choice(printable) for _ in xrange(100))
        user = User.objects.create_user(values['username'], values['email'], 
                                        rpwd)
        user.last_name = values['last_name']
        user.first_name = values['first_name']
        user.save()

    profile = user.get_profile()
    profile.registration = values['registration']
    profile.save()
    
    try:
        Inscription.objects.create(user=user, year=values['anac'],
                            section=values['facid'] + ':' + values['anet'])
    except:
        pass

    return user

def throw_b64error(request, raw):
    msg = b64encode(raw)
    msg = [ msg[y * 78:(y+1)*78] for y in xrange((len(msg)/78) +1) ]
    return render_to_response('error.html', {'msg': "\n".join(msg)},
                              context_instance=RequestContext(request))

def intranet_auth(request, next_url):
    sid, uid = request.GET.get("_sid", False), request.GET.get("_uid", False)
    if sid and uid:
        try:
            print ULB_AUTH % (sid, uid)
            verifier = urlopen(ULB_AUTH % (sid, uid))
            infos = verifier.read()
        except Exception as e:
            return render_to_response('error.html', 
                                      {'msg': "ulb timeout " + str(e)},
                                      context_instance=RequestContext(request))

        try:
            values = parse_user(infos)
            user = create_user(values)
        except Exception as e:
            return throw_b64error(request, infos + " -> " + str(e))

        user.backend = 'django.contrib.auth.backends.ModelBackend' 
        login(request, user)
        return HttpResponseRedirect(reverse('application') + '#' + next_url)
    else:
        return render_to_response('error.html', {'msg': 'url discarded'},
                                  context_instance=RequestContext(request))