# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest54643():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    return str(data), 200, {'Content-Type': 'text/html'}
