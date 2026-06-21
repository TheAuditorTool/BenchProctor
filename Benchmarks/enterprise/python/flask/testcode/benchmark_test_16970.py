# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest16970(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
