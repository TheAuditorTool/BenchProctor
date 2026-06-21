# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00599():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    int(str(data))
    return jsonify({"result": "success"})
