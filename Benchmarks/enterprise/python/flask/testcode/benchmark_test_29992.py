# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29992():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
