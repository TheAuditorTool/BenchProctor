# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18194():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
