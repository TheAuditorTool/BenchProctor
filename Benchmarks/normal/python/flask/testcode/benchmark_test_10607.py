# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10607():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
