# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest35210():
    redis_value = redis_client.get('user_data')
    try:
        data = json.loads(redis_value).get('value', redis_value)
    except (json.JSONDecodeError, AttributeError):
        data = redis_value
    json.loads(data)
    return jsonify({"result": "success"})
