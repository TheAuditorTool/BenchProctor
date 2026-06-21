# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket


def BenchmarkTest57179(path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
