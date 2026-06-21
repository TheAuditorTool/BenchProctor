# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import json
from app_runtime import auth_check


def BenchmarkTest39180():
    raw_body = request.get_data(as_text=True)
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
