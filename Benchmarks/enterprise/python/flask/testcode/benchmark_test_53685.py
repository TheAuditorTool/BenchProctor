# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53685():
    field_value = request.form.get('field', '')
    size = min(int(field_value) if str(field_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
