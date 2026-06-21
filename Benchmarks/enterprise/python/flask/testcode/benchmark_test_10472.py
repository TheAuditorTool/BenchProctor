# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10472():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
