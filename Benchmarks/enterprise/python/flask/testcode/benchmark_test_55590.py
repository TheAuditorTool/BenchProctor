# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest55590():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
