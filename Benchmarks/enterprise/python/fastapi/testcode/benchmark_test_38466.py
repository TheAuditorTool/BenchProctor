# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest38466(request: Request):
    ua_value = request.headers.get('user-agent', '')
    pending = list(str(ua_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
