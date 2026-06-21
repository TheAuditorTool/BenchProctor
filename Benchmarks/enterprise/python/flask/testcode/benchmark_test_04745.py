# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest04745():
    referer_value = request.headers.get('Referer', '')
    _resp = requests.get(str(referer_value))
    exec(_resp.text)
    return jsonify({"result": "success"})
