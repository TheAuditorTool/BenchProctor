# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest00882(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
