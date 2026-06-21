# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest68546():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
