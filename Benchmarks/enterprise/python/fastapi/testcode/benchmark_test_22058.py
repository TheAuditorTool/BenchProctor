# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest22058(request: Request):
    host_value = request.headers.get('host', '')
    db.execute('SELECT * FROM users WHERE id = ?', (host_value,))
    return {"updated": True}
