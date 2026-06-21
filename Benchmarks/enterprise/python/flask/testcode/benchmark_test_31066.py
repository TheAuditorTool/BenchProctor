# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31066():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
