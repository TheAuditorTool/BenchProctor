# SPDX-License-Identifier: Apache-2.0
import requests
from app_runtime import db


def BenchmarkTest38461():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
