# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest44137():
    upload_name = request.files['upload'].filename
    parsed = urlparse(upload_name)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = upload_name
    return '<script src="' + str(target_url) + '"></script>', 200, {'Content-Type': 'text/html'}
