# SPDX-License-Identifier: Apache-2.0
import requests
from app_runtime import db


def BenchmarkTest73593():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
