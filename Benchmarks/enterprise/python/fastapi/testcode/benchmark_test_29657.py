# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest29657(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
