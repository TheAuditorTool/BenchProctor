# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest63549():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return '<script src="' + str(target_url) + '"></script>', 200, {'Content-Type': 'text/html'}
