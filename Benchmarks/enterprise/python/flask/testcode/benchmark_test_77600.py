# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77600():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    int(str(data))
    return jsonify({"result": "success"})
