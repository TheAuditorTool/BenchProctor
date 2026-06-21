# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51137():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
