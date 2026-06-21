# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest70691(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
