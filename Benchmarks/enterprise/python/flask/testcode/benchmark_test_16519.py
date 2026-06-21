# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest16519():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
