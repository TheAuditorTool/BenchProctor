# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33162():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
