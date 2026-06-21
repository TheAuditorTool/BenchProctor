# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest65910(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
