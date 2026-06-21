# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25795():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    eval(str(data))
    return jsonify({"result": "success"})
