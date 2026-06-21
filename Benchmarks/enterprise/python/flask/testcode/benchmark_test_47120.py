# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest47120():
    raw_body = request.get_data(as_text=True)
    requests.post('https://api.prod.internal/data', data=str(raw_body), verify=True)
    return jsonify({"result": "success"})
