# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest35056(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
