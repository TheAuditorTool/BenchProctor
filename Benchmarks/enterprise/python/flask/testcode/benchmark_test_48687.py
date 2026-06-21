# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import requests


def BenchmarkTest48687():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
