# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest74411():
    referer_value = request.headers.get('Referer', '')
    data = default_blank(referer_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
