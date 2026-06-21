# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest65012():
    xml_value = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
