# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest40831(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
