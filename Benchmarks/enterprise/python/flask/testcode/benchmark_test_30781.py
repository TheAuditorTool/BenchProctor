# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest30781():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
