# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest50858(path_param):
    path_value = path_param
    data = unquote(path_value)
    exec(str(data))
    return jsonify({"result": "success"})
