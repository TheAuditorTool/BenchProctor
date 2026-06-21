# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest01112(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
