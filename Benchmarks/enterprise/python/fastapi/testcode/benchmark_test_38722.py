# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest38722(request: Request):
    ua_value = request.headers.get('user-agent', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(ua_value),))
    return {"updated": True}
