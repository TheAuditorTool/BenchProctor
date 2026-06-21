# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16003():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
