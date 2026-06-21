# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from flask import request, jsonify


def BenchmarkTest13172():
    field_value = request.form.get('field', '')
    parsed = urlparse(field_value)
    resolved = socket.gethostbyname(parsed.hostname or field_value)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = field_value.replace(parsed.hostname, resolved) if parsed.hostname else field_value
    requests.get(str(target_url))
    return jsonify({"result": "success"})
