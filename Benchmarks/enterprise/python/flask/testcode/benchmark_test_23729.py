# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest23729():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
