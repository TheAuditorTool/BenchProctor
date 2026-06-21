# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import json
from app_runtime import db


def BenchmarkTest54943():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
