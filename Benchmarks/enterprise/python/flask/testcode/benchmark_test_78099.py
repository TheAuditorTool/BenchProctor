# SPDX-License-Identifier: Apache-2.0
import secrets
import base64
from flask import request, jsonify


def BenchmarkTest78099():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
