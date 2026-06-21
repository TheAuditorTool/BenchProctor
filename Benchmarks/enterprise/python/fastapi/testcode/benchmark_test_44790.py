# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest44790(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    parts = str(profile_value).split(',')
    data = ','.join(parts)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
