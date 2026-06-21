# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def to_text(value):
    return str(value).strip()

def BenchmarkTest51092():
    referer_value = request.headers.get('Referer', '')
    data = to_text(referer_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
