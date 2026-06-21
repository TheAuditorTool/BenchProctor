# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def BenchmarkTest49398(path_param):
    path_value = path_param
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(path_value)).read()
    return jsonify({"result": "success"})
