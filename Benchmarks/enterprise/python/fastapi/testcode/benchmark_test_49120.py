# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest49120(request: Request):
    host_value = request.headers.get('host', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
