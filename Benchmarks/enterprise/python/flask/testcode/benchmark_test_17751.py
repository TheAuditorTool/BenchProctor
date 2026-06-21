# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17751():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
