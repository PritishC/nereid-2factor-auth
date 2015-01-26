# -*- coding: utf-8 -*-
"""
    user.py
    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Bool, Eval

__all__ = ['User']
__metaclass__ = PoolMeta


class User:
    __name__ = 'nereid.user'

    use_twofactor_auth = fields.Boolean('Use Two-Factor Auth')
    auth_method = fields.Selection([
        ('app_auth', 'Authentication Via App'),
        ('sms_auth', 'Authentication Via SMS'),
    ], 'Authentication Method', states={
        'readonly': ~Bool(Eval('use_twofactor_auth')),
    }, depends=['use_twofactor_auth']
    )

    @staticmethod
    def default_auth_method():
        return 'app_auth'
