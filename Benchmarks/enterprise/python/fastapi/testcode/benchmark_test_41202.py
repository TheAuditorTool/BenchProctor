# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest41202(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return {"updated": True}
