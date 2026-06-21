# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest55326(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = f'{profile_value}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
