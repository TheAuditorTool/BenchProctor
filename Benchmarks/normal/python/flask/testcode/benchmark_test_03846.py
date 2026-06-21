# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest03846():
    origin_value = request.headers.get('Origin', '')
    requests.get(str(origin_value))
    return jsonify({"result": "success"})
