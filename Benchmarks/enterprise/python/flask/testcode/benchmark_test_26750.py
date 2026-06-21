# SPDX-License-Identifier: Apache-2.0
import os
from app_runtime import db


def BenchmarkTest26750():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
