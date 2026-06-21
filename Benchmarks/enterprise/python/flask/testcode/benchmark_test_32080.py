# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest32080(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
