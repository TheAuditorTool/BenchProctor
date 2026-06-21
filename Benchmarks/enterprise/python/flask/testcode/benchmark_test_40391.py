# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40391():
    xml_value = request.get_data(as_text=True)
    parts = []
    for token in str(xml_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
