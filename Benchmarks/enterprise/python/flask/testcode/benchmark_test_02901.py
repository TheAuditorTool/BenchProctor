# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest02901():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
