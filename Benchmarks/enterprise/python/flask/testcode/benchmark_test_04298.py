# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04298():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
