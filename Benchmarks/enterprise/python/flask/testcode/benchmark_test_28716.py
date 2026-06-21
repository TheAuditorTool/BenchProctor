# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest28716():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
