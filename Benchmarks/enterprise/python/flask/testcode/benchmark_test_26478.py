# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest26478():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
