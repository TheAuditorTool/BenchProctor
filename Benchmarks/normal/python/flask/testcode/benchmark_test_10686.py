# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest10686():
    origin_value = request.headers.get('Origin', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
