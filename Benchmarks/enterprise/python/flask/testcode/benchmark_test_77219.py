# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import requests


def BenchmarkTest77219():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
