# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest29853(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
