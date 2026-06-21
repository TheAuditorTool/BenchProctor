# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17040():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
