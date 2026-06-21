# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest66112(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
