# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest00464():
    origin_value = request.headers.get('Origin', '')
    data = to_text(origin_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
