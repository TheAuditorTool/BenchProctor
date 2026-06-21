# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest49795():
    host_value = request.headers.get('Host', '')
    data = coalesce_blank(host_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
