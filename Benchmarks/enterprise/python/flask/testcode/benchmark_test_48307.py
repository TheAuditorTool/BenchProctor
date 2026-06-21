# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest48307(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
