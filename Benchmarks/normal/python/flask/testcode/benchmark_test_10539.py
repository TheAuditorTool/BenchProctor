# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest10539(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    os.seteuid(65534)
    return jsonify({"result": "success"})
