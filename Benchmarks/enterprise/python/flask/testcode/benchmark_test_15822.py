# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest15822():
    xml_value = request.get_data(as_text=True)
    data = normalise_input(xml_value)
    return jsonify({'error': 'An internal error occurred'}), 500
