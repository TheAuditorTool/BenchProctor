# SPDX-License-Identifier: Apache-2.0
import requests
from app_runtime import db


def BenchmarkTest58871():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    kind = 'json' if str(db_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = db_value
            data = parsed
        case _:
            data = db_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
