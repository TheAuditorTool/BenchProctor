# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest10492():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    requests.get(str(data))
    return jsonify({"result": "success"})
