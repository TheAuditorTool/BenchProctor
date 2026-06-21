# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest01261():
    auth_header = request.headers.get('Authorization', '')
    requests.get(str(auth_header))
    return jsonify({"result": "success"})
