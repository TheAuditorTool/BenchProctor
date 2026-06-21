# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest14256():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
