# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest01078():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
