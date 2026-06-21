# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80866():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
