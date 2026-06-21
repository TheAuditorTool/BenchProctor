# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest71100(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    db.execute('SELECT * FROM users WHERE id = ' + str(raw_body))
    return {"updated": True}
