# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24667():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
