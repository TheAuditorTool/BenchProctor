# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04659():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
