# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44027():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
