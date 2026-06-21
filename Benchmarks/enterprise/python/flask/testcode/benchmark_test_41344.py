# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
import socket
from app_runtime import mq_client


def relay_value(value):
    return value

def BenchmarkTest41344():
    msg_value = mq_client.get_message().body
    data = relay_value(msg_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
