# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest50449():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    def _primary():
        return Markup('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
