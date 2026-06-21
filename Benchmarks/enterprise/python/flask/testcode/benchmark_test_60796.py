# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest60796():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
