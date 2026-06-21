# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket


def BenchmarkTest65414(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
