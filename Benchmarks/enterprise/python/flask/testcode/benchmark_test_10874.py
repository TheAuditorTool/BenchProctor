# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import json
from app_runtime import db


def BenchmarkTest10874():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    return render_template_string(data)
