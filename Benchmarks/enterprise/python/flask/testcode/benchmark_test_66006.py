# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest66006():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
