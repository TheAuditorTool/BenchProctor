# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest20765():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
