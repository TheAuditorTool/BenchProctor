# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53349():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
