# SPDX-License-Identifier: Apache-2.0
import requests
from app_runtime import db


def BenchmarkTest08142():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
