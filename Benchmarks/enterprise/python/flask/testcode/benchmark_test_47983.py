# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47983():
    header_value = request.headers.get('X-Custom-Header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    int(str(data))
    return jsonify({"result": "success"})
