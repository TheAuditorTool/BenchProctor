# SPDX-License-Identifier: Apache-2.0
import json
import base64
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest75915():
    redis_value = redis_client.get('user_data')
    data = base64.b64decode(redis_value).decode('utf-8', 'ignore')
    json.loads(data)
    return jsonify({"result": "success"})
