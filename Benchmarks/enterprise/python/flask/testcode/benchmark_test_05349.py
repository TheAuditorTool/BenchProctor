# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05349():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
