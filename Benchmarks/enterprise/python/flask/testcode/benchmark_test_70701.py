# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest70701():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
