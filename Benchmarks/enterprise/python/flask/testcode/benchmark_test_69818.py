# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest69818():
    host_value = request.headers.get('Host', '')
    data = to_text(host_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
