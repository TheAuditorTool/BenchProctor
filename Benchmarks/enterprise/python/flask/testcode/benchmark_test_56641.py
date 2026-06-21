# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest56641(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
