# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest44845():
    header_value = request.headers.get('X-Custom-Header', '')
    data = coalesce_blank(header_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
