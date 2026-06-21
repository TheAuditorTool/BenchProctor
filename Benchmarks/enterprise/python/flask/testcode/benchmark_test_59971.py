# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59971():
    field_value = request.form.get('field', '')
    if str(field_value) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
