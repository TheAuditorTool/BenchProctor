# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest06288():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
