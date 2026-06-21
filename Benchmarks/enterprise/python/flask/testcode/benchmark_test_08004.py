# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest08004():
    referer_value = request.headers.get('Referer', '')
    data = normalise_input(referer_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
