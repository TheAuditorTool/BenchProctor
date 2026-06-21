# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import jsonify
import socket
from app_runtime import db


def BenchmarkTest20725():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
