# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest11274():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    return jsonify({'error': 'An internal error occurred'}), 500
