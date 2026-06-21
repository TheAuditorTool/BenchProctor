# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from flask import request, jsonify


def BenchmarkTest72945():
    header_value = request.headers.get('X-Custom-Header', '')
    parsed = urlparse(header_value)
    resolved = socket.gethostbyname(parsed.hostname or header_value)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = header_value.replace(parsed.hostname, resolved) if parsed.hostname else header_value
    requests.get(str(target_url))
    return jsonify({"result": "success"})
