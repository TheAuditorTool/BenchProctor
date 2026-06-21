# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest39019(request: Request):
    host_value = request.headers.get('host', '')
    pending = list(str(host_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
