# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest30935():
    raw_body = request.get_data(as_text=True)
    data = default_blank(raw_body)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
