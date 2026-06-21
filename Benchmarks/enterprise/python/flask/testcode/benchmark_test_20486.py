# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest20486():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
