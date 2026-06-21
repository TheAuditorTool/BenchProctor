# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest39936():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
