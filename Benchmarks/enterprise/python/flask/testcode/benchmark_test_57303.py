# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from app_runtime import db


def BenchmarkTest57303():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % str(db_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
