# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30999():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
