# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30548():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
