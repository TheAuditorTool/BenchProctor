# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44765():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
