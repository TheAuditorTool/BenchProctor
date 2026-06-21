# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56538():
    xml_value = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(xml_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
