# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14820():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
