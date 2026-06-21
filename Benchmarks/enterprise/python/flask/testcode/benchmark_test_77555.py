# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest77555():
    redis_value = redis_client.get('user_data')
    data = f'{redis_value:.200s}'
    json.loads(data)
    return jsonify({"result": "success"})
