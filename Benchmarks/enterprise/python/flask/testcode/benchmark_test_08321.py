# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08321():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
