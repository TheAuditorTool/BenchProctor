# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import ipaddress
import socket
import requests
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest01011():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = RequestPayload(api_value).value
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
