# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest22631(path_param):
    path_value = path_param
    result = 100 / int(str(path_value))
    return jsonify({"result": "success"})
