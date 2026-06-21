# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


def BenchmarkTest03882(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
