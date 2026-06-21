# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import ipaddress
import socket
from flask import request, jsonify


def BenchmarkTest52576():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
