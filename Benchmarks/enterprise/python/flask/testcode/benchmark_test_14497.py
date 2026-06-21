# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest14497():
    redis_value = redis_client.get('user_data')
    kind = 'json' if str(redis_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = redis_value
            data = parsed
        case _:
            data = redis_value
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
