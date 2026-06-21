# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
import json
from flask import request, jsonify


def BenchmarkTest23519():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
