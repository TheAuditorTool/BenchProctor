# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket
from app_runtime import mq_client


def BenchmarkTest60047():
    msg_value = mq_client.get_message().body
    prefix = ''
    data = prefix + str(msg_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
