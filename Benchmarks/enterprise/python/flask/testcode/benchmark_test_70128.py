# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70128():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
