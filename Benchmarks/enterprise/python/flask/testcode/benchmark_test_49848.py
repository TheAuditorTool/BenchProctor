# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest49848(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    os.remove(str(data))
    return jsonify({"result": "success"})
