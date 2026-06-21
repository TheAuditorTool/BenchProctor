# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import base64
from app_runtime import db


def BenchmarkTest11136():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    return Markup('<div>' + str(data) + '</div>')
