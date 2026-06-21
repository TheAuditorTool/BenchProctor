# SPDX-License-Identifier: Apache-2.0
import base64
from flask import jsonify
import socket
from app_runtime import mq_client


def BenchmarkTest11585():
    msg_value = mq_client.get_message().body
    data = base64.b64decode(msg_value).decode('utf-8', 'ignore')
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
