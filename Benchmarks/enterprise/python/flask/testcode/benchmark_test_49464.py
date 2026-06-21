# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49464():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    return jsonify({'error': 'An internal error occurred'}), 500
