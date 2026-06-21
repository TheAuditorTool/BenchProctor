# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest68161(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
