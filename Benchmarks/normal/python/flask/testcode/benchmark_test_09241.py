# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest09241():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
