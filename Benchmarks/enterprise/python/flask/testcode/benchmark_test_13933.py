# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest13933(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
