# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08597():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
