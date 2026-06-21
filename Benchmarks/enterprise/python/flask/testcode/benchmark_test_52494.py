# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle
from app_runtime import redis_client


def BenchmarkTest52494():
    redis_value = redis_client.get('user_data')
    parts = str(redis_value).split(',')
    data = ','.join(parts)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
