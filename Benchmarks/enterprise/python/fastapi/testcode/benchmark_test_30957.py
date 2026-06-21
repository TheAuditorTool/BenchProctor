# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest30957(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
