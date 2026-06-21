# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import jsonify
from app_runtime import db


def BenchmarkTest55390():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parsed = urlparse(comment_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = comment_value
    return '<script src="' + str(target_url) + '"></script>', 200, {'Content-Type': 'text/html'}
