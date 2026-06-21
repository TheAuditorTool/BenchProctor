# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from app_runtime import db


def BenchmarkTest57613():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    prefix = ''
    data = prefix + str(db_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
