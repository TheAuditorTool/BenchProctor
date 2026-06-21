# SPDX-License-Identifier: Apache-2.0
import os
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest42428():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
