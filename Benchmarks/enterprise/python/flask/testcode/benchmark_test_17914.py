# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest17914():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    reader = make_reader(secret_value)
    data = reader()
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
