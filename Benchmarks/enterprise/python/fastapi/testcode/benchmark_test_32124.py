# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest32124(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    requests.post('https://api.prod.internal/data', data=str(profile_value), verify=True)
    return {"updated": True}
