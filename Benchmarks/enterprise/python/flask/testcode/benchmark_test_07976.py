# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07976():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
