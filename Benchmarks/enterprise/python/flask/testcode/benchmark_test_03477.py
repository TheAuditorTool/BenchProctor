# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest03477(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
