# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest72306(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return jsonify({"result": "success"})
