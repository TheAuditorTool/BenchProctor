# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import jsonify
import ast
from app_runtime import mq_client


def BenchmarkTest72459():
    msg_value = mq_client.get_message().body
    try:
        data = str(ast.literal_eval(msg_value))
    except (ValueError, SyntaxError):
        data = msg_value
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
