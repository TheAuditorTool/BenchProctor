# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest02031():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
