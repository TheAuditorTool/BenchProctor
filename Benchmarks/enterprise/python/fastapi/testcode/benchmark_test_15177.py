# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest15177(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(forwarded_ip),))
    return {"updated": True}
