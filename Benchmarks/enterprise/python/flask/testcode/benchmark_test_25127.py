# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest25127(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
