# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest06187():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    _ev = {}
    eval(compile("link_path = os.path.join('/var/app/data', str(data))\ntarget = os.readlink(link_path)\nwith open(target, 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
