# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61705():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return str(processed), 200, {'Content-Type': 'text/html'}
