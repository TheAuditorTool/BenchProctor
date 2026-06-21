# SPDX-License-Identifier: Apache-2.0
import json
from app_runtime import db


def BenchmarkTest69140():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
