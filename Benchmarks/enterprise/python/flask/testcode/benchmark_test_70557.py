# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket
from app_runtime import redis_client


def ensure_str(value):
    return str(value)

def BenchmarkTest70557():
    redis_value = redis_client.get('user_data')
    data = ensure_str(redis_value)
    processed = data[:64]
    s = socket.create_connection((str(processed), 80))
    s.close()
    return jsonify({"result": "success"})
