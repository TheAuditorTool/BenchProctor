# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest07971():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
