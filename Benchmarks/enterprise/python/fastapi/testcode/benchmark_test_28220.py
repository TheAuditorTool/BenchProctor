# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest28220(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
