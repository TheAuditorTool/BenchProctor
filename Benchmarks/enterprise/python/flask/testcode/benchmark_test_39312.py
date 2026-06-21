# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39312():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
