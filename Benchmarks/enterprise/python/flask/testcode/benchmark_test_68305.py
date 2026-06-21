# SPDX-License-Identifier: Apache-2.0
import json
from app_runtime import db


def BenchmarkTest68305():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
