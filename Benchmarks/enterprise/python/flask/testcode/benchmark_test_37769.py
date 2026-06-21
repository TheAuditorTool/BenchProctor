# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37769():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    exec(str(data))
    return jsonify({"result": "success"})
