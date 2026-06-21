# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest31437(path_param):
    path_value = path_param
    os.remove(str(path_value))
    return jsonify({"result": "success"})
