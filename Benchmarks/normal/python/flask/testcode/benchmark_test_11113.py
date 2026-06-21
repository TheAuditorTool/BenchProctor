# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket
from app_runtime import redis_client


def BenchmarkTest11113():
    redis_value = redis_client.get('user_data')
    data, _sep, _rest = str(redis_value).partition('\x00')
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
