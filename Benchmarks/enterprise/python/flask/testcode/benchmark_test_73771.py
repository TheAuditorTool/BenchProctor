# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73771():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    int(str(data))
    return jsonify({"result": "success"})
