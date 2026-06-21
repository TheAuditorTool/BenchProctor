# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest02814():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
