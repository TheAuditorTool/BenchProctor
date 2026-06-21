# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79032():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    eval(str(data))
    return jsonify({"result": "success"})
