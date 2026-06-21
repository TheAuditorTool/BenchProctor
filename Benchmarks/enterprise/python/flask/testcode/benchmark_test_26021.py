# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest26021():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
