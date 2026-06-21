# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30651():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
