# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest01871():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
