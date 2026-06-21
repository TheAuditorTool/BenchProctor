# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest01757():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = default_blank(forwarded_ip)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
