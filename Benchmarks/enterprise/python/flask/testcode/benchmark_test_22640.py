# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest22640():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    def _primary():
        return Markup('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
