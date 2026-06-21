# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68970():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
