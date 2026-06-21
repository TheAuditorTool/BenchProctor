# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest13121():
    host_value = request.headers.get('Host', '')
    data = default_blank(host_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
