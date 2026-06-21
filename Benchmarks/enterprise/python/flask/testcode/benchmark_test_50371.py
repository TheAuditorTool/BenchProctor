# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50371():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
