# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest40228():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
