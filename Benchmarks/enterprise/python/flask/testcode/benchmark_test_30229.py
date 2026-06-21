# SPDX-License-Identifier: Apache-2.0
import requests
import json
from app_runtime import db


def BenchmarkTest30229():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
