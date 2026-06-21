# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
from app_runtime import db


def BenchmarkTest00516():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
