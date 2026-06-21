# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest70908():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
