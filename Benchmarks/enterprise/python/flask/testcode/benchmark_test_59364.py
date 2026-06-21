# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest59364():
    redis_value = redis_client.get('user_data')
    data = '%s' % str(redis_value)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
