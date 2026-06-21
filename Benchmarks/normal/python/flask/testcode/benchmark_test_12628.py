# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12628():
    multipart_value = request.form.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
