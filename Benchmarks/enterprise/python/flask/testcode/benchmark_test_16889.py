# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16889():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
