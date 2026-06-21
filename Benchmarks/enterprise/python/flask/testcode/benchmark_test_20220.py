# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest20220():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
