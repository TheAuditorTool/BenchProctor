# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest19464():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
