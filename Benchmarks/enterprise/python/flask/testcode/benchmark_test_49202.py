# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest49202():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = handle(db_value)
    _ev = {}
    eval(compile('_ev[\'r\'] = Markup(\'<img src="\' + str(data) + \'">\')', '<sink>', 'exec'))
    return _ev['r']
