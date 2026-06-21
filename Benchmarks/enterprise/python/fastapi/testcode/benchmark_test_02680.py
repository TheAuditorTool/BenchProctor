# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest02680(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    def _primary():
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
