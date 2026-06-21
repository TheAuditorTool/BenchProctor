# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest00116():
    ua_value = request.headers.get('User-Agent', '')
    data = to_text(ua_value)
    _ev = {}
    eval(compile("with open(os.path.join('/var/app/data', str(data)), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
