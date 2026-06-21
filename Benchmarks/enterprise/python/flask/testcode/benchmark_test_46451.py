# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46451():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
