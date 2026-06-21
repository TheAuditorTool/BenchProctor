# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26715():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
