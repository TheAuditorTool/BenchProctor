# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest81447():
    redis_value = redis_client.get('user_data')
    kind = 'json' if str(redis_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = redis_value
            data = parsed
        case _:
            data = redis_value
    json.loads(data)
    return jsonify({"result": "success"})
