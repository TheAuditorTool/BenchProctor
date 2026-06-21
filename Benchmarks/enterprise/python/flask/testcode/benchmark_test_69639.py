# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69639():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
