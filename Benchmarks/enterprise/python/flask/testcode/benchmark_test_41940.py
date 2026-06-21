# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest41940():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = normalise_input(json_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
