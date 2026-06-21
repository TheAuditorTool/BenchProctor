# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest61373():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
