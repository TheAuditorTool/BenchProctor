# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest61670(request: Request):
    origin_value = request.headers.get('origin', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(origin_value),))
    return {"updated": True}
