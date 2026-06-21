# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79978():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
