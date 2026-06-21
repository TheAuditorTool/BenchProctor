# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest45583():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    auth_check('user', data)
    return jsonify({"result": "success"})
