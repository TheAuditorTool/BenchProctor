# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80052():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
