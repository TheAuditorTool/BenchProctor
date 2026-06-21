# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest45022():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    requests.get(str(json_value))
    return jsonify({"result": "success"})
