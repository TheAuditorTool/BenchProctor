# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04272():
    ua_value = request.headers.get('User-Agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
