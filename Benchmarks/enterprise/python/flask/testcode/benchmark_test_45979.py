# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest45979():
    redis_value = redis_client.get('user_data')
    data, _sep, _rest = str(redis_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
