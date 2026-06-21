# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest69362(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
