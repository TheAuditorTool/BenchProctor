# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest64934(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
