# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest58571():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
