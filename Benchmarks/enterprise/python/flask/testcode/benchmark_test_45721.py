# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
import socket
from app_runtime import redis_client


def BenchmarkTest45721():
    redis_value = redis_client.get('user_data')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(redis_value)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        s = socket.create_connection((str(data), 80))
        s.close()
    return jsonify({"result": "success"})
