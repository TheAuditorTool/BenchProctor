# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05839():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
