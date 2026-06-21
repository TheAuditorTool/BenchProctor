# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest33631():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    requests.post('http://api.prod.internal/data', data=str(target_url))
    return jsonify({"result": "success"})
