# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54004():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
