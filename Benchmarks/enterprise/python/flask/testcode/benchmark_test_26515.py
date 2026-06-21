# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
from app_runtime import redis_client


def BenchmarkTest26515():
    redis_value = redis_client.get('user_data')
    data = '%s' % (redis_value,)
    json.loads(data)
    return jsonify({"result": "success"})
