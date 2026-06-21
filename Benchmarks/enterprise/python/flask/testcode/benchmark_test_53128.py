# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest53128():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
