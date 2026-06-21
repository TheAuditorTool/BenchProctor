# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42963():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    return jsonify({'error': 'An internal error occurred'}), 500
