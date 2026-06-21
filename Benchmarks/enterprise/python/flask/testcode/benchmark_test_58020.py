# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest58020():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
