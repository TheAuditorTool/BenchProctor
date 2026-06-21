# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68162():
    xml_value = request.get_data(as_text=True)
    return jsonify({'error': str(xml_value), 'stack': repr(locals())}), 500
