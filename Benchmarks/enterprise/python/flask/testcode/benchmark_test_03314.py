# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest03314(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    os.remove(str(data))
    return jsonify({"result": "success"})
