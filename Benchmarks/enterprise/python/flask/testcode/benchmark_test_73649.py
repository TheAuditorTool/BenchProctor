# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest73649():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
