# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest55614():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = normalise_input(forwarded_ip)
    processed = data[:64]
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
