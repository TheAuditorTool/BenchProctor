# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest06649(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
