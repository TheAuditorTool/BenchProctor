# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest43382(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    requests.get(str(data))
    return jsonify({"result": "success"})
