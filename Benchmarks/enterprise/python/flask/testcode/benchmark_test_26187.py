# SPDX-License-Identifier: Apache-2.0
import os
from app_runtime import db


def BenchmarkTest26187():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
