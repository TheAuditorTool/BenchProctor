# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest09643(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
