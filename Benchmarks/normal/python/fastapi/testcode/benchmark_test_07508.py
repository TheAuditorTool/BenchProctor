# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest07508(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(raw_body),))
    return {"updated": True}
