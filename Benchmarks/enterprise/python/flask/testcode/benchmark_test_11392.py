# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest11392():
    raw_body = request.get_data(as_text=True)
    data = relay_value(raw_body)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
