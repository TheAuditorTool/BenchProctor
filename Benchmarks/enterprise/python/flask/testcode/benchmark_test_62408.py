# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import redis_client


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest62408():
    redis_value = redis_client.get('user_data')
    ctx = RequestContext(redis_value)
    data = ctx.payload
    yaml.safe_load(data)
    return jsonify({"result": "success"})
