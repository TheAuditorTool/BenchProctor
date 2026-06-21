# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest44900(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
