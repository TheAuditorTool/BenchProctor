# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest01885():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
