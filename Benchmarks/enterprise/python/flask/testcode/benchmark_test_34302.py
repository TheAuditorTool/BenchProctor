# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest34302():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
