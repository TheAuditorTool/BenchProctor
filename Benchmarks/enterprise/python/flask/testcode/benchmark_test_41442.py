# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest41442():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
