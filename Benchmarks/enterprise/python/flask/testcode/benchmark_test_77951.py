# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import jsonify
from app_runtime import db


def BenchmarkTest77951():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return jsonify({"result": "success"})
