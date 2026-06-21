# SPDX-License-Identifier: Apache-2.0
import os
from app_runtime import db


def BenchmarkTest38460():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
