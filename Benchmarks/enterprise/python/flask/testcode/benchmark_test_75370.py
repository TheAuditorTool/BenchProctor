# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest75370():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
