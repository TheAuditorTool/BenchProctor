# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05793():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    return jsonify({'error': 'An internal error occurred'}), 500
