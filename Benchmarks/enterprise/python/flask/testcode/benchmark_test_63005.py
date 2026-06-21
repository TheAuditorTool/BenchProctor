# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63005():
    xml_value = request.get_data(as_text=True)
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
