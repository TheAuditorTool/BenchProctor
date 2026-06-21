# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest01080(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
