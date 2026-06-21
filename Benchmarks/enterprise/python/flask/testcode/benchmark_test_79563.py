# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79563():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
