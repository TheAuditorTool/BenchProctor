# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest10240():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
