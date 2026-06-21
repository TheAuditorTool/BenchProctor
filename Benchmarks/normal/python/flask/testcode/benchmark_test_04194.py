# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest04194():
    redis_value = redis_client.get('user_data')
    data = redis_value if redis_value else 'default'
    yaml.safe_load(data)
    return jsonify({"result": "success"})
