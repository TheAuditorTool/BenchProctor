# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest28755():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
