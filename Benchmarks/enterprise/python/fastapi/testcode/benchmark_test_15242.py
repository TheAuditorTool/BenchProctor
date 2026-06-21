# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest15242(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
