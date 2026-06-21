# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
from app_runtime import db


def BenchmarkTest16601():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    prefix = ''
    data = prefix + str(db_value)
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
