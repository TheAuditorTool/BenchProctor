# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18505():
    field_value = request.form.get('field', '')
    if not str(field_value).isdigit():
        raise ValueError('invalid input: ' + str(field_value))
    return jsonify({"result": "success"})
