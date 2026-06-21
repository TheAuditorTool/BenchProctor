# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket
from app_runtime import mq_client


def BenchmarkTest66805():
    msg_value = mq_client.get_message().body
    kind = 'json' if str(msg_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = msg_value
            data = parsed
        case _:
            data = msg_value
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
