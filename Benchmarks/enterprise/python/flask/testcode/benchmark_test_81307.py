# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest81307(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    os.remove(str(data))
    return jsonify({"result": "success"})
