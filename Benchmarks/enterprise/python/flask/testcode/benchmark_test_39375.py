# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest39375():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
