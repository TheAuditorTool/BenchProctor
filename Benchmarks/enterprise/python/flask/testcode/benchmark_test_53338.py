# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest53338():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
