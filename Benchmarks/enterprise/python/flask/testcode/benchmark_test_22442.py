# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22442():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
