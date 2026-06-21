# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest57034():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = str(json_value).replace('\x00', '')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
