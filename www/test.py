# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 23:48:30 2016

@author: diffe
"""

import orm
from models import User, Blog, Comment

def test():
    yield from orm.create_pool(user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

for x in test():
    pass