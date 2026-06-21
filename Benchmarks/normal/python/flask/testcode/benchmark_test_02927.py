# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest02927(path_param):
    path_value = path_param
    data = unquote(path_value)
    eval(str(data))
    return jsonify({"result": "success"})
