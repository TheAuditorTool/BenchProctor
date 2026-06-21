# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest67989(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
