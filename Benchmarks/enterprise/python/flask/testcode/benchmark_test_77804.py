# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77804():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
