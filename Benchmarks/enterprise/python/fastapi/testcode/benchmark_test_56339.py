# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest56339(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
