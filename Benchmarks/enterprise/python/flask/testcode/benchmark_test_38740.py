# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest38740(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
