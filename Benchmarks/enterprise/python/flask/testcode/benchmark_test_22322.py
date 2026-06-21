# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest22322(path_param):
    path_value = path_param
    requests.get('https://api.pycdn.io/data', params={'q': str(path_value)}, verify=True)
    return jsonify({"result": "success"})
