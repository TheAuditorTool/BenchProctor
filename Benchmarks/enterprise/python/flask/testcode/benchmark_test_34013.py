# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import redis_client


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest34013():
    redis_value = redis_client.get('user_data')
    data = default_blank(redis_value)
    eval(compile('yaml.load(data, Loader=yaml.UnsafeLoader)', '<sink>', 'exec'))
    return jsonify({"result": "success"})
