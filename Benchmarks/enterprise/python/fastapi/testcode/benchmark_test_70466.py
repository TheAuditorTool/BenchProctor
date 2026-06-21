# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest70466(request: Request):
    origin_value = request.headers.get('origin', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(origin_value),))
    return {"updated": True}
