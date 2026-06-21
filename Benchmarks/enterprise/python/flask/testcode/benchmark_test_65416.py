# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest65416(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    os.remove(str(data))
    return jsonify({"result": "success"})
