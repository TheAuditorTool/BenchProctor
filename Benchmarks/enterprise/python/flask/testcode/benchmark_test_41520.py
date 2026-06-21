# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from app_runtime import db


def BenchmarkTest41520():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
