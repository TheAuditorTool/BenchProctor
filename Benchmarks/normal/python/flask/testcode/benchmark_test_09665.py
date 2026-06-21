# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle
from app_runtime import redis_client


def BenchmarkTest09665():
    redis_value = redis_client.get('user_data')
    data = redis_value.decode('utf-8', 'ignore') if isinstance(redis_value, bytes) else redis_value
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
