# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest51242(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
