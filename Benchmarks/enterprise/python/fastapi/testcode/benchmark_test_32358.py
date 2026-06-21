# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest32358(request: Request):
    host_value = request.headers.get('host', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(host_value),))
    return {"updated": True}
