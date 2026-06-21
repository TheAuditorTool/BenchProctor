# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37259():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    return jsonify({'error': 'An internal error occurred'}), 500
