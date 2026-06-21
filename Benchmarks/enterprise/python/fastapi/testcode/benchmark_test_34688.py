# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest34688(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
