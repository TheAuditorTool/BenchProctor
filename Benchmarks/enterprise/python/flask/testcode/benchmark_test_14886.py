# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest14886():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    return str(data), 200, {'Content-Type': 'text/html'}
