# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52674():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
