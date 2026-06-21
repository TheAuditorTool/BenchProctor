# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest05599():
    referer_value = request.headers.get('Referer', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(referer_value)}, verify=True)
    return jsonify({"result": "success"})
