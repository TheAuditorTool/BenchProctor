# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40188():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
