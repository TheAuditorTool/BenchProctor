# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53831():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
