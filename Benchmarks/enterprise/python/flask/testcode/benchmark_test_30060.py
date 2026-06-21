# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest30060(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
