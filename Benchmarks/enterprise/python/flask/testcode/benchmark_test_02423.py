# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02423():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
