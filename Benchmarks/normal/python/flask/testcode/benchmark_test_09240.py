# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest09240(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
