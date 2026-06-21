# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76034():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
