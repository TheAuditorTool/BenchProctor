# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29186():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
