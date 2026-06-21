# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58991():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    eval(str(data))
    return jsonify({"result": "success"})
