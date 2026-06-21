# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import os
from flask import jsonify


def BenchmarkTest68362():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return '<script src="' + str(target_url) + '"></script>', 200, {'Content-Type': 'text/html'}
