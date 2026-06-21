# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21086():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
