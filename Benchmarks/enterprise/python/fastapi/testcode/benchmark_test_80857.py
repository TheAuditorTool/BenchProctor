# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest80857(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    if profile_value:
        data = profile_value
    else:
        data = ''
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
