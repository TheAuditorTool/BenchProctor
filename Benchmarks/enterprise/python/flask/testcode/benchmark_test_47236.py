# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest47236(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    requests.get(str(data))
    return jsonify({"result": "success"})
