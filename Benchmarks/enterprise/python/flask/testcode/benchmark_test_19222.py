# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest19222():
    referer_value = request.headers.get('Referer', '')
    data = relay_value(referer_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
