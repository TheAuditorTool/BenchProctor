# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest80818(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
