# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41569():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
