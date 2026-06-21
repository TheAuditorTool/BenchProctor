# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest59112():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    return str(data), 200, {'Content-Type': 'text/html'}
