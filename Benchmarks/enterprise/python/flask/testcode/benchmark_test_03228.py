# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest03228():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
