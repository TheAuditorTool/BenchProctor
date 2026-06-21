# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02224():
    field_value = request.form.get('field', '')
    if len(str(field_value)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
