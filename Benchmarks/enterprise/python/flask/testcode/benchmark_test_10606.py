# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket


def BenchmarkTest10606(path_param):
    path_value = path_param
    data = f'{path_value}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
