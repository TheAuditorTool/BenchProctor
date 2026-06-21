# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10247():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value}'
    return jsonify({'error': 'An internal error occurred'}), 500
