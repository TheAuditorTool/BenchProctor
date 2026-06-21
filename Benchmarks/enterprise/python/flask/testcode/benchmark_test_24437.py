# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest24437():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = default_blank(forwarded_ip)
    _ev = {}
    eval(compile("with open(os.path.join('/var/app/data', str(data)), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
