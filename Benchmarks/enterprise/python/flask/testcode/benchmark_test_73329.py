# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest73329():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
