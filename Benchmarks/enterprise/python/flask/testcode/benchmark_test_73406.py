# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
import os
from flask import jsonify


def BenchmarkTest73406():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
