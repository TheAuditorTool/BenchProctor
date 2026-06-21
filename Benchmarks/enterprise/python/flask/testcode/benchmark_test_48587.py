# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import json
from app_runtime import db


def BenchmarkTest48587():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    return Markup('<img src="' + str(data) + '">')
