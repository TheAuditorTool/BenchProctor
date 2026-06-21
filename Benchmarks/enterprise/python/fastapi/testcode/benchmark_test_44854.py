# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest44854(request: Request):
    referer_value = request.headers.get('referer', '')
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(referer_value)))
    return {"updated": True}
