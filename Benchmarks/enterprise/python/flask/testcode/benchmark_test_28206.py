# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28206():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
