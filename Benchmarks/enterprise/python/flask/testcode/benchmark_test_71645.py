# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest71645():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
