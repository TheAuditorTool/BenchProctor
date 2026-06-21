# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59384():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
