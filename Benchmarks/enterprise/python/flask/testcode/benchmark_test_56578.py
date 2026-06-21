# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest56578(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
