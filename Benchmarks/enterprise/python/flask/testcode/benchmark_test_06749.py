# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest06749():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
