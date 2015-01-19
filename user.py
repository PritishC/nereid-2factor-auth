# -*- coding: utf-8 -*-
"""
    user.py
    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import PoolMeta

__all__ = ['User']
__metaclass__ = PoolMeta


class User:
    __name__ = 'nereid.user'
