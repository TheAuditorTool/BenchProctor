# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest54150():
    host_value = request.headers.get('Host', '')
    data = normalise_input(host_value)
    int(str(data))
    return jsonify({"result": "success"})
