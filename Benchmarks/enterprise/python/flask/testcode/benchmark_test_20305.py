# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
import base64
from flask import request, jsonify


def BenchmarkTest20305():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
