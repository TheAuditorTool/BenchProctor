# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest77084():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
