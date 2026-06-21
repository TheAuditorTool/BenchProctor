# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest28935(path_param):
    path_value = path_param
    requests.get(str(path_value))
    return jsonify({"result": "success"})
