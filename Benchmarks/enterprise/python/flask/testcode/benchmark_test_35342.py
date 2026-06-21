# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest35342():
    redis_value = redis_client.get('user_data')
    data = redis_value.decode('utf-8', 'ignore') if isinstance(redis_value, bytes) else redis_value
    json.loads(data)
    return jsonify({"result": "success"})
