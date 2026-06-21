# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest43895():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
