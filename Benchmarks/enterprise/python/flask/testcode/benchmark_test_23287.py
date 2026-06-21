# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest23287(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
