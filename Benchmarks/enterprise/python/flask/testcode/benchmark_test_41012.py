# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41012():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    eval(str(data))
    return jsonify({"result": "success"})
