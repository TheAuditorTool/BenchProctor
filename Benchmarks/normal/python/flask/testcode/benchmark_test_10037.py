# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from flask import jsonify
from app_runtime import mq_client


def BenchmarkTest10037():
    msg_value = mq_client.get_message().body
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(msg_value)
    data = collected
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
