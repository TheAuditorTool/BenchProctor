# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest01782():
    origin_value = request.headers.get('Origin', '')
    data = normalise_input(origin_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
