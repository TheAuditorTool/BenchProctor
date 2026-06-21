# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest46533():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ensure_str(forwarded_ip)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
