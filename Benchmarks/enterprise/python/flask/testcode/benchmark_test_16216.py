# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest16216(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
