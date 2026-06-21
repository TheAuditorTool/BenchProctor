# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73540():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
