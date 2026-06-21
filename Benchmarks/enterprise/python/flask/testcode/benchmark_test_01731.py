# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest01731():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    _ev = {}
    eval(compile("_ev['r'] = Markup('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
