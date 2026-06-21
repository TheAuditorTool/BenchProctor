# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest60203():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
