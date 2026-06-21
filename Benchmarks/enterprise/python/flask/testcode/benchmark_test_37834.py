# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest37834():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    with open('/var/app/data/' + str(db_value), 'r') as fh:
        content = fh.read()
    return content
