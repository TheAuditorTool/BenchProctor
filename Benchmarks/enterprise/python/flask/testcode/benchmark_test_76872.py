# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76872():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    int(str(data))
    return jsonify({"result": "success"})
