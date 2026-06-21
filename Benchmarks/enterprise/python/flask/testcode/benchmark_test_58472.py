# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest58472():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    return str(data), 200, {'Content-Type': 'text/html'}
