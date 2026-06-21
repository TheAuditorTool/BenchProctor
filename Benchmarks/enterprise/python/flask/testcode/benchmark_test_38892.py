# SPDX-License-Identifier: Apache-2.0
import os
from app_runtime import db


def BenchmarkTest38892():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = str(db_value).replace('\x00', '')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
