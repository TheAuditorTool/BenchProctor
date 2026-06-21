# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def relay_value(value):
    return value

def BenchmarkTest49258():
    ua_value = request.headers.get('User-Agent', '')
    data = relay_value(ua_value)
    def _primary():
        return Markup('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
