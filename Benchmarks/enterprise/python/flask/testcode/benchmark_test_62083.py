# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62083():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
