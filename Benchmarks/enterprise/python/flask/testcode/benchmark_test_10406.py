# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10406():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
