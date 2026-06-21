# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest02557(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
