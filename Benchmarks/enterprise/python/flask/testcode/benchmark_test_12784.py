# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12784():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
