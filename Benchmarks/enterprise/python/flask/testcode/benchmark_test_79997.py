# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest79997():
    auth_header = request.headers.get('Authorization', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
