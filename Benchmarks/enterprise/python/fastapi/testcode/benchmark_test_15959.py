# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest15959(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(header_value),))
    return {"updated": True}
