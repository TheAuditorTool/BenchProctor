# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest75816():
    origin_value = request.headers.get('Origin', '')
    data = normalise_input(origin_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
