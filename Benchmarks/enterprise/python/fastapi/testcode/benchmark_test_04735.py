# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest04735(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
