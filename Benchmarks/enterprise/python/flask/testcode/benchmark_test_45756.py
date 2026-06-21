# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest45756():
    header_value = request.headers.get('X-Custom-Header', '')
    data = normalise_input(header_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
