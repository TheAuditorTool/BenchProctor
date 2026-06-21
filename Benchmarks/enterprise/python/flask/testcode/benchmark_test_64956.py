# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64956():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
