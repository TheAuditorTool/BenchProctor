# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest12229():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile('_ev[\'r\'] = Markup(\'<img src="\' + str(data) + \'">\')', '<sink>', 'exec'))
    return _ev['r']
