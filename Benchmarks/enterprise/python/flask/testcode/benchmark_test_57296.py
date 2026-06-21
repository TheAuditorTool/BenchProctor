# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest57296(path_param):
    path_value = path_param
    data = f'{path_value}'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
