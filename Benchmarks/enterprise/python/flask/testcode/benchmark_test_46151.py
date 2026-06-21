# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46151():
    xml_value = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
