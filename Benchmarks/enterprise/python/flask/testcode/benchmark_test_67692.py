# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import jsonify
import socket
from app_runtime import redis_client


def BenchmarkTest67692():
    redis_value = redis_client.get('user_data')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(redis_value)
    data = collected
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
