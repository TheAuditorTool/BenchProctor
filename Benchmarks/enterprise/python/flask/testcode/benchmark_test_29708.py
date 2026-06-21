# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest29708():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
