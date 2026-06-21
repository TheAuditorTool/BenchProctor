# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest38361():
    raw_body = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
