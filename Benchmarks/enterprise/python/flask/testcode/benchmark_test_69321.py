# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest69321(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
