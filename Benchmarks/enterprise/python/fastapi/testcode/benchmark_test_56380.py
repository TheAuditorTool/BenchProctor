# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest56380(request: Request):
    ua_value = request.headers.get('user-agent', '')
    db.execute('SELECT * FROM users WHERE id = ' + str(ua_value))
    return {"updated": True}
