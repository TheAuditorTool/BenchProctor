# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest00861(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
