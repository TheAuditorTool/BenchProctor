# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest39451():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
