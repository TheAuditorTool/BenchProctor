# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest28847(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
