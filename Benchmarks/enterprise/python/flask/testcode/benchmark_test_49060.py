# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest49060():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    return str(data), 200, {'Content-Type': 'text/html'}
