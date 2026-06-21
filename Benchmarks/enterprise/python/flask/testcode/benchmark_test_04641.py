# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest04641():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
