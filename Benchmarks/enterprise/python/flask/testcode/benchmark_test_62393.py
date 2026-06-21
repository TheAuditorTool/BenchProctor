# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest62393():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
