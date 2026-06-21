# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest00923(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
