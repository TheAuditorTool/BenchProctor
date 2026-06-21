# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from flask import jsonify
from app_runtime import redis_client


def BenchmarkTest33090():
    redis_value = redis_client.get('user_data')
    parsed = urlparse(redis_value)
    resolved = socket.gethostbyname(parsed.hostname or redis_value)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = redis_value.replace(parsed.hostname, resolved) if parsed.hostname else redis_value
    requests.get(str(target_url))
    return jsonify({"result": "success"})
