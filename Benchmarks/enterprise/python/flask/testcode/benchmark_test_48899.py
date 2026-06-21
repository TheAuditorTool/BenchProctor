# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48899():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
