# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest48178():
    header_value = request.headers.get('X-Custom-Header', '')
    requests.get(str(header_value))
    return jsonify({"result": "success"})
