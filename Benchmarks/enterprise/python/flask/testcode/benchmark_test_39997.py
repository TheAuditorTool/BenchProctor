# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39997():
    xml_value = request.get_data(as_text=True)
    if xml_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = xml_value
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
