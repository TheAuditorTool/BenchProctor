# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest09906(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
