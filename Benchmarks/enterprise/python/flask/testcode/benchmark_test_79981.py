# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79981():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
