# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07117(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
