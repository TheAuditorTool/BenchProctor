# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest59259():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
