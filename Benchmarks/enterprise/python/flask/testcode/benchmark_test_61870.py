# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61870():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
