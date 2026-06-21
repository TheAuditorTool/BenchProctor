# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest55671(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    os.remove(str(data))
    return jsonify({"result": "success"})
