# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest59629(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
