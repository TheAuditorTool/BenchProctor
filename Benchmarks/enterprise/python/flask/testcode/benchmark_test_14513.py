# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14513():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
