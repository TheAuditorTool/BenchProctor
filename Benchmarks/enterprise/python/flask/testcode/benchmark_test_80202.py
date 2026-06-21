# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def normalise_input(value):
    return value.strip()

def BenchmarkTest80202():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    _ev = {}
    eval(compile("_ev['r'] = Markup('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
