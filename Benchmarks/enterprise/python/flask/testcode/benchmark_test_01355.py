# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify


def BenchmarkTest01355():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
