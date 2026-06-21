# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest01745():
    referer_value = request.headers.get('Referer', '')
    data = default_blank(referer_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
