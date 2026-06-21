# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31891():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
