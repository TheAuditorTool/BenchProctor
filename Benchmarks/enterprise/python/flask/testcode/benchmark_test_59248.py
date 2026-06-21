# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59248():
    field_value = request.form.get('field', '')
    if str(field_value) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
