# SPDX-License-Identifier: Apache-2.0
import os
from app_runtime import db


def BenchmarkTest06688():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    checked_path = os.path.join('/var/app/data', os.path.basename(comment_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
