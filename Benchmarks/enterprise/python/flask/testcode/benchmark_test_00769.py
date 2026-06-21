# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00769():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
