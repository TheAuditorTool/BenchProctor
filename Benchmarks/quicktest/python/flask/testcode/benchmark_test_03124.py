# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest03124(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
