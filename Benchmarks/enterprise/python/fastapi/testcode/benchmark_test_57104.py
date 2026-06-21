# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest57104(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
