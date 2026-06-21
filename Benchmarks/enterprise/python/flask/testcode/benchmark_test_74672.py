# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


def BenchmarkTest74672():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ','.join(parts)
    return Markup('<div>' + str(data) + '</div>')
