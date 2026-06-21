# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest04861(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
