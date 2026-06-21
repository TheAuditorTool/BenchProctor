# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest21333():
    redis_value = redis_client.get('user_data')
    data = json.loads(redis_value).get('value', '')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
