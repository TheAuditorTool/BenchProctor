# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest45099():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
