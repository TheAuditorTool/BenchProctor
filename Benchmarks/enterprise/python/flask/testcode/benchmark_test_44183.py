# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44183():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
