# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest08144():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
