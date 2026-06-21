# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest11433():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    auth_check('user', data)
    return jsonify({"result": "success"})
