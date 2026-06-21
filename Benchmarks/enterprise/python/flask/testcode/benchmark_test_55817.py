# SPDX-License-Identifier: Apache-2.0
import os
from app_runtime import db


def BenchmarkTest55817():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    checked_path = os.path.join('/var/app/data', os.path.basename(db_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
