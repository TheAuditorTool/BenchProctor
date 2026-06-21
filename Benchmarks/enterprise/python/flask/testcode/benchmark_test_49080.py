# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest49080(path_param):
    path_value = path_param
    data = unquote(path_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
