# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import os
from flask import jsonify


def BenchmarkTest46177():
    env_value = os.environ.get('USER_INPUT', '')
    parsed = urlparse(env_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = env_value
    requests.get(str(target_url))
    return jsonify({"result": "success"})
