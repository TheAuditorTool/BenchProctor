# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20090():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
