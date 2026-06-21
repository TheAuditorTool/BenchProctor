# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32192():
    host_value = request.headers.get('Host', '')
    int(str(host_value))
    return jsonify({"result": "success"})
