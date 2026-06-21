# SPDX-License-Identifier: Apache-2.0
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest65792():
    host_value = request.headers.get('Host', '')
    data = to_text(host_value)
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
