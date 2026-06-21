# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75101():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
