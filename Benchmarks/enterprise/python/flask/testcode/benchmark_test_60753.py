# SPDX-License-Identifier: Apache-2.0
import os
from app_runtime import db


def BenchmarkTest60753():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
