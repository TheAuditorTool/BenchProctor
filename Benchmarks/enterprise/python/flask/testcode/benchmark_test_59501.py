# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import json
from app_runtime import auth_check


def BenchmarkTest59501():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
