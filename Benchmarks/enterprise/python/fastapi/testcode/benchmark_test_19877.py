# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest19877(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
