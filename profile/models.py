# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.contrib.contenttypes.generic import GenericForeignKey
from django.db.models.signals import post_save, post_syncdb
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from permission.models import Permission
from django.db.models import Q
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    registration = models.CharField(max_length=80)
    welcome = models.BooleanField(default=True)
    comment = models.TextField(null=True)
    photo = models.CharField(max_length=80, null=True)

    def perm(self, name, oid=0):
        perm = Permission.objects.filter(name=name, user=self.user)
        return perm.filter(Q(object_id=oid) | Q(object_id=0)).count() > 0

    def real_name(self):
        return self.user.first_name + " " + self.user.last_name
    

class Following(models.Model):
    user = models.ForeignKey(User)
    foll_oid = models.PositiveIntegerField()
    foll_content = models.ForeignKey(ContentType)
    follow = GenericForeignKey('foll_content', 'foll_oid')
    last_visit = models.DateTimeField(auto_now_add=True, null=False)
    visited = models.IntegerField(default=0, null=False)

    class Meta:
        unique_together = ('user', 'foll_oid', 'foll_content')


class Inscription(models.Model):
    user = models.ForeignKey(User)
    section = models.CharField(max_length=80, null=True)
    year = models.PositiveIntegerField(null=True)

    class Meta:
        unique_together = ('user', 'section', 'year')

# for all user creation, create profile with default value
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, registration=0)

post_save.connect(create_user_profile, sender=User)

# hack to prevent ./manage syncdb to ask for a superusers
from django.contrib.auth.management import create_superuser
from django.contrib.auth import models as auth_app
post_syncdb.disconnect(create_superuser, sender=auth_app,
                       dispatch_uid="django.contrib.auth.management.create_superuser")
