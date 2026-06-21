# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest40726(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
