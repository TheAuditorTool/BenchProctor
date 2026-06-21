# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest43907(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = default_blank(db_value)
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
