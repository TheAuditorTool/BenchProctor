# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


def BenchmarkTest04014():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    return Markup('<div>' + str(data) + '</div>')
