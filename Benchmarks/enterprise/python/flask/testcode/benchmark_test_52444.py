# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest52444():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    session['data'] = str(data)
    return jsonify({"result": "success"})
