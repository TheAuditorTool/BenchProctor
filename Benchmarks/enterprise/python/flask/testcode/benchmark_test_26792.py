# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest26792(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    eval(str(data))
    return jsonify({"result": "success"})
