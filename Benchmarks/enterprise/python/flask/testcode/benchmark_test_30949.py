# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest30949():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
