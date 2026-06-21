# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21740():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
