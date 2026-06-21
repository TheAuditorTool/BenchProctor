# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import json


def BenchmarkTest75879():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
