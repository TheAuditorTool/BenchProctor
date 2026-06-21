# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest15504(path_param):
    path_value = path_param
    data = unquote(path_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
