# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35685():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
