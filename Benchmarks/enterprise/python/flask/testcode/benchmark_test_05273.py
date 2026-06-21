# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest05273():
    ua_value = request.headers.get('User-Agent', '')
    data = default_blank(ua_value)
    _ev = {}
    eval(compile("with open(os.path.join('/var/app/data', str(data)), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
