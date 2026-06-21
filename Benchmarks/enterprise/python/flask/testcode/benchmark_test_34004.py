# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest34004():
    ua_value = request.headers.get('User-Agent', '')
    data = to_text(ua_value)
    processed = data[:64]
    if str(processed) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
