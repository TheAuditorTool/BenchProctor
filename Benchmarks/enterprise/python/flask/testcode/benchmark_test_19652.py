# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest19652():
    field_value = request.form.get('field', '')
    data = to_text(field_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
