# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest46376():
    redis_value = redis_client.get('user_data')
    data = (lambda v: v.strip())(redis_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
