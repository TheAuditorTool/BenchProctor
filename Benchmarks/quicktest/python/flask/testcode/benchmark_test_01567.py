# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest01567():
    redis_value = redis_client.get('user_data')
    def normalize(value):
        return value.strip()
    data = normalize(redis_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
