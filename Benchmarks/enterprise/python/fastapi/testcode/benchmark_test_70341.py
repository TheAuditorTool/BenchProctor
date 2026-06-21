# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest70341(request: Request):
    referer_value = request.headers.get('referer', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(referer_value),))
    return {"updated": True}
