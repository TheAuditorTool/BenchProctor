# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03899():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = default_blank(db_value)
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
