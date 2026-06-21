# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest63573():
    raw_body = request.get_data(as_text=True)
    requests.get('https://api.pycdn.io/data', params={'q': str(raw_body)}, verify=False)
    return jsonify({"result": "success"})
