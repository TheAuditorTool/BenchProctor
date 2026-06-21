# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import requests


def BenchmarkTest11855(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
