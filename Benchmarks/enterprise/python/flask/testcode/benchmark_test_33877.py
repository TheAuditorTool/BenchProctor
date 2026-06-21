# SPDX-License-Identifier: Apache-2.0
import requests
from app_runtime import db


def BenchmarkTest33877():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return '<script src="' + str(db_value) + '"></script>', 200, {'Content-Type': 'text/html'}
