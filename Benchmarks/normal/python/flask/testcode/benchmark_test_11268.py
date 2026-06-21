# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest11268():
    ua_value = request.headers.get('User-Agent', '')
    data = normalise_input(ua_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
