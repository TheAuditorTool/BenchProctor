# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest79970(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
