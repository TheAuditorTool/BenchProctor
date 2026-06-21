# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80291():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
