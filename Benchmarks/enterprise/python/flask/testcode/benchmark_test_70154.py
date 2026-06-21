# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70154():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
