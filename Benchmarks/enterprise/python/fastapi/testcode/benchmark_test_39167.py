# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest39167(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    pending = list(str(profile_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
