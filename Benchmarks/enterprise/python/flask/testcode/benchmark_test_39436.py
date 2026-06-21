# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest39436(path_param):
    path_value = path_param
    data = unquote(path_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
