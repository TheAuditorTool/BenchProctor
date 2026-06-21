# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52310():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
