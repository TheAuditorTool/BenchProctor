# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13398():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    eval(str(data))
    return jsonify({"result": "success"})
