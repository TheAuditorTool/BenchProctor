# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest09451():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
