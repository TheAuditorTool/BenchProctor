# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest38786(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
