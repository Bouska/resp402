#!/usr/bin/env python

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from os import environ
environ.setdefault('DJANGO_SETTINGS_MODULE', 'www.settings')

from category.models import Category, CategoryItem
from group.models import Group
from course.models import Course

c1 = Course.objects.create(slug='info-f-666', name='Hell Informatique', 
                           description='Hell Computer Science course')
c2 = Course.objects.create(slug='math-h-708', name='Over Math', 
                           description='New math course based on fuzzy axiomes')

g1 = Group.objects.create(slug='CI', name='Cercle Informatique',
                          description='Cercle des etudiants en info \o/')
g2 = Group.objects.create(slug='ACE', name='Association des Cercles Etudiants',
                          description='Youplaboom')

cat0 = Category.objects.create(name='Faculty', description='Root node w/ category')
cat1 = Category.objects.create(name='Sciences', description='Fac de sciences')
cat2 = Category.objects.create(name='Polytech', description='Polytech')
cat3 = Category.objects.create(name='Informatique', description='Section INFO')

cat0.holds.add(cat1)
cat0.holds.add(cat2)
cat1.holds.add(cat3)

CategoryItem.objects.create(category=cat3, thing=c1, priority=1)
CategoryItem.objects.create(category=cat3, thing=c2, priority=2)
CategoryItem.objects.create(category=cat3, thing=g1, priority=3)
CategoryItem.objects.create(category=cat0, thing=g2, priority=1)
