# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest44731(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    os.seteuid(65534)
    return jsonify({"result": "success"})
