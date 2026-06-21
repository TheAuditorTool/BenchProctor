# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest02599(path_param):
    path_value = path_param
    data = unquote(path_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
