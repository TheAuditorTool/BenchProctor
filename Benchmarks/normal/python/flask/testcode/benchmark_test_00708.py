# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle
from app_runtime import redis_client


def BenchmarkTest00708():
    redis_value = redis_client.get('user_data')
    if redis_value:
        data = redis_value
    else:
        data = ''
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
