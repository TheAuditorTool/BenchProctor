# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10301():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    eval(str(data))
    return jsonify({"result": "success"})
