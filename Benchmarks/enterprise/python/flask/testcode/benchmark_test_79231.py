# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest79231():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
