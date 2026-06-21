# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from flask import request, jsonify


def BenchmarkTest71419():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parsed = urlparse(forwarded_ip)
    resolved = socket.gethostbyname(parsed.hostname or forwarded_ip)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = forwarded_ip.replace(parsed.hostname, resolved) if parsed.hostname else forwarded_ip
    requests.get(str(target_url))
    return jsonify({"result": "success"})
