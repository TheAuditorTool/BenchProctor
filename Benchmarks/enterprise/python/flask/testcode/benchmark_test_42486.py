# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42486():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
