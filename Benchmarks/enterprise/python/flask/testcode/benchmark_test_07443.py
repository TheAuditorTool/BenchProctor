# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest07443(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
