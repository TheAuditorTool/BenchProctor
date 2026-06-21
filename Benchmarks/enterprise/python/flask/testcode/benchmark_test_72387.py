# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest72387(path_param):
    path_value = path_param
    data = ensure_str(path_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
