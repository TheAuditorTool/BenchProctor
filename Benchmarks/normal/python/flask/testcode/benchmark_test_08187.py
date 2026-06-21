# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest08187(path_param):
    path_value = path_param
    requests.get(str(path_value))
    return jsonify({"result": "success"})
