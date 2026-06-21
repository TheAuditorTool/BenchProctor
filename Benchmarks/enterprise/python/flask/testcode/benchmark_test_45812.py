# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest45812():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
