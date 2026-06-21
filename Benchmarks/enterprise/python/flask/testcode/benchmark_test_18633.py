# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest18633():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
