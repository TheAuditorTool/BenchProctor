# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest08766(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.remove(str(data))
    return jsonify({"result": "success"})
