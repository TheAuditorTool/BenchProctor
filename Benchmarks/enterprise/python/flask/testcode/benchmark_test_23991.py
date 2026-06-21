# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23991():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    return jsonify({'error': 'An internal error occurred'}), 500
