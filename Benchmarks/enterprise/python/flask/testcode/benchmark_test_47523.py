# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import ipaddress
import socket
from flask import jsonify
from app_runtime import mq_client


def BenchmarkTest47523():
    msg_value = mq_client.get_message().body
    parts = []
    for token in str(msg_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
