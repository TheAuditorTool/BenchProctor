# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest03133():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
