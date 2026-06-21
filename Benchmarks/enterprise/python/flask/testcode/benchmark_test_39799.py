# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest39799():
    host_value = request.headers.get('Host', '')
    data = coalesce_blank(host_value)
    _ev = {}
    eval(compile("_ev['r'] = Markup('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
