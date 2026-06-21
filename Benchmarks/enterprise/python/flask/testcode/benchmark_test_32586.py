# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32586():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    eval(str(data))
    return jsonify({"result": "success"})
