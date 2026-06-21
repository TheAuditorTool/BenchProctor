# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest74862():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    requests.get(str(data))
    return jsonify({"result": "success"})
