# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest16565():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
