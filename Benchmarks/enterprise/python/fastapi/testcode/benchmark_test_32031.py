# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest32031(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
