# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest67174(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
