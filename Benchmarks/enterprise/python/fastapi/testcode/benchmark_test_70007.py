# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest70007(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    parts = []
    for token in str(profile_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
