# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04609():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
