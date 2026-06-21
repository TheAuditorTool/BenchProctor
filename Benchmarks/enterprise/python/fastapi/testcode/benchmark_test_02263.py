# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest02263(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
