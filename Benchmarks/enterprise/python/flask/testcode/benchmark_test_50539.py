# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest50539():
    ua_value = request.headers.get('User-Agent', '')
    data = coalesce_blank(ua_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
