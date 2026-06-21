# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest52320():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = normalise_input(json_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
