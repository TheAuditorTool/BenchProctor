# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest48982():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    int(str(data))
    return jsonify({"result": "success"})
