# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle
from app_runtime import redis_client


def BenchmarkTest31629():
    redis_value = redis_client.get('user_data')
    pickle.loads(redis_value.encode('latin-1'))
    return jsonify({"result": "success"})
