# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest80549(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
