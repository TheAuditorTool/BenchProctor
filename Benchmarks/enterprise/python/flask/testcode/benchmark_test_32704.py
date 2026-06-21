# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32704():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
