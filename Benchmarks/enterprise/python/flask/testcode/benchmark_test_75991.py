# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest75991():
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    return jsonify({'error': 'An internal error occurred'}), 500
