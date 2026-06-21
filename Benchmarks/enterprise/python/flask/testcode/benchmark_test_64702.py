# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest64702():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
