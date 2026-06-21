# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest50488(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
