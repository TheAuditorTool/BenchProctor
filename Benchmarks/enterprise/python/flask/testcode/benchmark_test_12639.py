# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import json


def BenchmarkTest12639():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
