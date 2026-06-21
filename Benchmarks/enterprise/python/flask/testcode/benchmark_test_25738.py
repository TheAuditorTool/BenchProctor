# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25738():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
