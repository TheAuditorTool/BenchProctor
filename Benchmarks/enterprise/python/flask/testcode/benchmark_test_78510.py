# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78510():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    exec(str(data))
    return jsonify({"result": "success"})
