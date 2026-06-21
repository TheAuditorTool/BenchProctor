# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest00084():
    referer_value = request.headers.get('Referer', '')
    data = normalise_input(referer_value)
    return jsonify({'error': 'An internal error occurred'}), 500
