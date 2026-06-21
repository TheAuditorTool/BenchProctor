# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54402():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
