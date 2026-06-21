# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40351():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
