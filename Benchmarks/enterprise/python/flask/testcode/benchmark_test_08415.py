# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest08415():
    xml_value = request.get_data(as_text=True)
    data = ensure_str(xml_value)
    return jsonify({'error': 'An internal error occurred'}), 500
