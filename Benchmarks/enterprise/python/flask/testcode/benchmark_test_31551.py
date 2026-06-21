# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest31551():
    ua_value = request.headers.get('User-Agent', '')
    data = ensure_str(ua_value)
    _ev = {}
    eval(compile("link_path = os.path.join('/var/app/data', str(data))\ntarget = os.readlink(link_path)\nwith open(target, 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
