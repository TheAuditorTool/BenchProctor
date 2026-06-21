# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket
from app_runtime import redis_client


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest55517():
    redis_value = redis_client.get('user_data')
    data = RequestPayload(redis_value).value
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
