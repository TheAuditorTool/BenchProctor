# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest81443(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    pending = list(str(db_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    json.loads(data)
    return {"updated": True}
