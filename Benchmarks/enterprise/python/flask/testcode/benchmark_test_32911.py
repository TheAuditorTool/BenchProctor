# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest32911(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
