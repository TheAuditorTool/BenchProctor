# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest81142():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
