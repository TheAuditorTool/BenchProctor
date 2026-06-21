# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27696():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
