# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70826():
    xml_value = request.get_data(as_text=True)
    return jsonify({'error': 'An internal error occurred'}), 500
