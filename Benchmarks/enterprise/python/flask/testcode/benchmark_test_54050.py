# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest54050(path_param):
    path_value = path_param
    size = min(int(path_value) if str(path_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
