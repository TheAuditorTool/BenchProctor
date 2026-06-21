# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from flask import request, jsonify


def BenchmarkTest12462():
    origin_value = request.headers.get('Origin', '')
    parsed = urlparse(origin_value)
    resolved = socket.gethostbyname(parsed.hostname or origin_value)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = origin_value.replace(parsed.hostname, resolved) if parsed.hostname else origin_value
    requests.get(str(target_url))
    return jsonify({"result": "success"})
