# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09945():
    field_value = request.form.get('field', '')
    data = bytearray(int(field_value) if str(field_value).isdigit() else 0)
    return jsonify({"result": "success"})
