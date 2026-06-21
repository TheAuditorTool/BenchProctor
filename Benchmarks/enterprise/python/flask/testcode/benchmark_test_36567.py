# SPDX-License-Identifier: Apache-2.0
import yaml
from dataclasses import dataclass
from flask import jsonify
from app_runtime import redis_client


@dataclass
class FormData:
    payload: str

def BenchmarkTest36567():
    redis_value = redis_client.get('user_data')
    data = FormData(payload=redis_value).payload
    yaml.safe_load(data)
    return jsonify({"result": "success"})
