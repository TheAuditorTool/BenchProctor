# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import urllib.request


def BenchmarkTest59853():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
