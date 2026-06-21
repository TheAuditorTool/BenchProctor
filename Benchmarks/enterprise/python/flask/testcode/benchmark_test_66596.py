# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest66596():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
