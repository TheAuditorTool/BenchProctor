# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from app_runtime import db


async def BenchmarkTest02741(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
