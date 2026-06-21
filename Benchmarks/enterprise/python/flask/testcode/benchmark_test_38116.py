# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest38116():
    raw_body = request.get_data(as_text=True)
    requests.get('https://api.pycdn.io/data', params={'q': str(raw_body)}, verify=True)
    return jsonify({"result": "success"})
