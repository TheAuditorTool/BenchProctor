# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def BenchmarkTest01046():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(json_value)).read()
    return jsonify({"result": "success"})
