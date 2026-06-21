# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37254():
    host_value = request.headers.get('Host', '')
    result = 100 / int(str(host_value))
    return jsonify({"result": "success"})
