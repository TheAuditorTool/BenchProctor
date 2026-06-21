# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from flask import jsonify
from types import SimpleNamespace
from app_runtime import mq_client


def BenchmarkTest07245():
    msg_value = mq_client.get_message().body
    ns = SimpleNamespace(payload=msg_value)
    data = getattr(ns, 'payload')
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return jsonify({'error': 'private range blocked'}), 403
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
