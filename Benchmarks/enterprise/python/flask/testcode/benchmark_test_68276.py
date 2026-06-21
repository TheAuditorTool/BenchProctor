# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68276():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
