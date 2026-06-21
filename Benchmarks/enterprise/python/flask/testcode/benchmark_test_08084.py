# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest08084():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
