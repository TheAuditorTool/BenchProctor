# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest28022(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
