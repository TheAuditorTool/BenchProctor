# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest70121(request: Request):
    origin_value = request.headers.get('origin', '')
    db.execute('SELECT * FROM users WHERE id = ?', (origin_value,))
    return {"updated": True}
