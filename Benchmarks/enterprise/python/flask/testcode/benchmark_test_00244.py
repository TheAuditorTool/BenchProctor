# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import json
from app_runtime import db


def BenchmarkTest00244():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    return Markup('<div>' + str(data) + '</div>')
