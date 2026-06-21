# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify


def BenchmarkTest38317():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
