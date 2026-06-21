# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest01521(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
