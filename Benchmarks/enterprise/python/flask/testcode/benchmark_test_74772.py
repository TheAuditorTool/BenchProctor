# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74772():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    int(str(data))
    return jsonify({"result": "success"})
