# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46459():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500
