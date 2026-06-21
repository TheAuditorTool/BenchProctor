# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import socket


def BenchmarkTest37789():
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
