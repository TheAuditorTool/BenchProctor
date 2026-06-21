# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest79544(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
