# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest75042():
    auth_header = request.headers.get('Authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
