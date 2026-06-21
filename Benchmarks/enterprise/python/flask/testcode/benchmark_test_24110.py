# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


def BenchmarkTest24110():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return Markup('<div>' + str(db_value) + '</div>')
