# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest42365(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    eval(str(data))
    return jsonify({"result": "success"})
