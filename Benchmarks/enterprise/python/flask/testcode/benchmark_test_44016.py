# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44016():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
