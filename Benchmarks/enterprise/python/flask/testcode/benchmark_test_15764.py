# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
import pickle
from app_runtime import redis_client


def BenchmarkTest15764():
    redis_value = redis_client.get('user_data')
    data = json.loads(redis_value).get('value', '')
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
