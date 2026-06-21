# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest22819():
    xml_value = request.get_data(as_text=True)
    data = coalesce_blank(xml_value)
    return jsonify({'error': 'An internal error occurred'}), 500
