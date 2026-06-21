# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest28532(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
