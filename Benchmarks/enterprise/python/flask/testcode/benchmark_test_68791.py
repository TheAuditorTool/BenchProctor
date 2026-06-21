# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest68791():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
