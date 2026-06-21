# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest08874(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    eval(str(data))
    return jsonify({"result": "success"})
