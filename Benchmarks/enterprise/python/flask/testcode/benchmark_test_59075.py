# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59075():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    int(str(data))
    return jsonify({"result": "success"})
