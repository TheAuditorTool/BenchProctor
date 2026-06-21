# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54089():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
