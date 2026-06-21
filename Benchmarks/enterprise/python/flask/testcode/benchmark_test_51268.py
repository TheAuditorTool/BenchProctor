# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest51268():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with open('/var/app/data/' + str(comment_value), 'r') as fh:
        content = fh.read()
    return content
