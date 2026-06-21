# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest17446(path_param):
    path_value = path_param
    _resp = requests.get(str(path_value))
    exec(_resp.text)
    return jsonify({"result": "success"})
