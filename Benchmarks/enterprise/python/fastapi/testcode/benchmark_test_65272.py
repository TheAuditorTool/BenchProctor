# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest65272(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
