# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13047():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
