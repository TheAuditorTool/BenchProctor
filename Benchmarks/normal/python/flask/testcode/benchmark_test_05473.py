# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import jsonify
import socket
from app_runtime import mq_client


def BenchmarkTest05473():
    msg_value = mq_client.get_message().body
    data = msg_value if msg_value else 'default'
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
