# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest07210():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    _resp = requests.get(str(forwarded_ip))
    exec(_resp.text)
    return jsonify({"result": "success"})
