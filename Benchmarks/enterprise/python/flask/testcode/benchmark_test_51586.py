# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest51586():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
