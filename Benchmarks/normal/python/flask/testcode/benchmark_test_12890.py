# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
import socket
from app_runtime import mq_client


def to_text(value):
    return str(value).strip()

def BenchmarkTest12890():
    msg_value = mq_client.get_message().body
    data = to_text(msg_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
