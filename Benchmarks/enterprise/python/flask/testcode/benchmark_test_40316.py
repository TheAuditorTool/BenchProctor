# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def to_text(value):
    return str(value).strip()

def BenchmarkTest40316():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = to_text(json_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
