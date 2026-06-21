# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest74141(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = default_blank(ua_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
