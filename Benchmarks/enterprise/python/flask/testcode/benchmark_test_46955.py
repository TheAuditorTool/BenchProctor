# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46955():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
