# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest69301():
    referer_value = request.headers.get('Referer', '')
    data = coalesce_blank(referer_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
